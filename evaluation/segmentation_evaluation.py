
import os
import cv2
import random
import warnings
import argparse
import glob

import numpy as np

from sklearn.metrics import jaccard_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score

random.seed(0)
np.random.seed(0)

warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser(description="")

parser.add_argument("-i", "--submission-dir", type=str)
parser.add_argument("-o", "--output-dir", type=str)
parser.add_argument("-t", "--truth-dir", type=str)

SUPPORTED_FILETYPES = [".jpg", ".jpeg", ".png"]
CSV_VAL_ORDER = ["accuracy", "jaccard", "dice", "f1", "recall", "precision"]

def read_mask(path):
    mask = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if mask.max() > 127:
        mask = mask / 255.0
    mask = mask > 0.5
    mask = mask.astype(np.uint8)
    mask = mask.reshape(-1)
    return mask

def filter_filtypes(path):
    _, fileext = os.path.splitext(path)
    return fileext in SUPPORTED_FILETYPES

def dice_score(y_true, y_pred):
    return np.sum(y_pred[y_true == 1] == 1) * 2.0 / (np.sum(y_pred[y_pred == 1] == 1) + np.sum(y_true[y_true == 1] == 1))

def calculate_metrics(y_true, y_pred):
    score_accuracy = accuracy_score(y_true, y_pred)
    score_jaccard = jaccard_score(y_true, y_pred, average="binary")
    score_f1 = f1_score(y_true, y_pred, average="binary")
    score_recall = recall_score(y_true, y_pred, average="binary")
    score_precision = precision_score(y_true, y_pred, average="binary", zero_division=0)
    score_dice = dice_score(y_true, y_pred)
    return [score_accuracy, score_jaccard, score_dice, score_f1, score_recall, score_precision]

def get_filename(filepath):
    return os.path.splitext(os.path.basename(filepath))[0]

def invert_mask(mask):
    _mask = mask.copy()
    mask[_mask == 1] = 0
    mask[_mask == 0] = 1
    return mask

def evaluate_submission(submission_dir, output_dir, ground_truth_dir):

    submission_attributes = os.path.basename(submission_dir).split("_")
    
    team_name = submission_attributes[1]
    run_id = "_".join(submission_attributes[2:-1])
    task_name = submission_attributes[-1]

    team_result_path = os.path.join(output_dir, team_name, task_name, run_id)

    if not os.path.exists(team_result_path):
        os.makedirs(team_result_path)
        
    true_masks = sorted(glob.glob(os.path.join(ground_truth_dir, "*")))

    pred_masks = sorted(glob.glob(os.path.join(submission_dir, "*")))
    pred_masks = list(filter(filter_filtypes, pred_masks))

    mean_score = []

    detailed_metrics_filename = "%s_%s_%s_detailed_metrics.csv" % (team_name, task_name, run_id)
    average_metrics_filename = "%s_%s_%s_average_metrics.csv" % (team_name, task_name, run_id)

    with open(os.path.join(team_result_path, detailed_metrics_filename), "w") as f:

        f.write("filename;%s\n" % ";".join(CSV_VAL_ORDER))

        assert len(true_masks) == len(pred_masks)

        for index, (y_true_path, y_pred_path) in enumerate(zip(true_masks, pred_masks)):

            print("Progress [%i / %i]" % (index + 1, len(true_masks)), end="\r")
            
            assert get_filename(y_true_path) == get_filename(y_pred_path)

            y_true = read_mask(y_true_path)
            y_pred = read_mask(y_pred_path)

            if y_true.max() == 0:
                y_true = invert_mask(y_true)
                y_pred = invert_mask(y_pred)

            metrics = calculate_metrics(y_true, y_pred)

            results_line = "%s;" % get_filename(y_true_path)
            results_line += ";".join(["%0.4f" % score for score in metrics])
            results_line += "\n"
            
            f.write(results_line)

            mean_score.append(metrics)

        print("\n")

    mean_score = np.mean(mean_score, axis=0)

    with open(os.path.join(team_result_path, average_metrics_filename), "w") as f:
        f.write("metric;value\n")
        f.write("\n".join(["%s;%0.4f" % (header, score) for header, score in zip(CSV_VAL_ORDER, mean_score)]))

    with open(os.path.join(output_dir, "%s_all_average_metrics.csv" % task_name), "a") as f:
        f.write("%s;%s;%s;" % (team_name, task_name, run_id))
        f.write(";".join(["%0.4f" % score for score in mean_score]))
        f.write("\n")

if __name__ == "__main__":

    args = parser.parse_args()

    submission_dir = args.submission_dir
    output_dir = args.output_dir
    truth_dir = args.truth_dir

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(os.path.join(output_dir, "%s_all_average_metrics.csv" % os.path.basename(submission_dir)), "w") as f:
        f.write("team-name;task-name;run-id;%s\n" % ";".join(CSV_VAL_ORDER)) 

    for submission_dir in glob.glob(os.path.join(submission_dir, "*")):
        print("Evaluating %s..." % submission_dir)
        evaluate_submission(submission_dir, output_dir, truth_dir)