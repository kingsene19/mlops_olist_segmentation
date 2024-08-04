#! /bin/bash

EXECUTION_DATE=$(date "+%Y%m%d-%H%M")
YEAR=$(date "+%Y")
MONTH=$(date "+%m")

PROJECT_DIR=$PWD
LOGS_DIR=${PROJECT_DIR}/logs/${YEAR}/${MONTH}
ANALYSIS_DIR=${LOGS_DIR}/analysis
TRAINING_DIR=${LOGS_DIR}/training
STABILITY_DIR=${LOGS_DIR}/stability

mkdir -p ${LOGS_DIR}
mkdir -p ${ANALYSIS_DIR}
mkdir -p ${TRAINING_DIR}
mkdir -p ${STABILITY_DIR}

cd notebooks

echo "==================== Début analyse ======================"
papermill segmentation_01_analyse.ipynb "${ANALYSIS_DIR}/${EXECUTION_DATE}-olist-analysis-artifcat.ipynb" --report-mode --log-output --no-progress-bar

if [ $? -ne 0 ]; then
    echo "ERROR: Echec survenu pendant l'analyse"
    exit 1
fi
echo "==================== Analyse Terminé ======================"

echo "==================== Début entrainement modèle ======================"
papermill segmentation_02_essais.ipynb "${TRAINING_DIR}/${EXECUTION_DATE}-olist-training-artifcat.ipynb" --report-mode --log-output --no-progress-bar

if [ $? -ne 0 ]; then
    echo "ERROR: Echec survenu pendant l'entrainement"
    exit 1
fi
echo "==================== Entrainement Terminé ======================"

# echo "==================== Début stabilité ======================"
papermill segmentation_03_stabilite.ipynb "${STABILITY_DIR}/${EXECUTION_DATE}-olist-stability-artifcat.ipynb" --report-mode --log-output --no-progress-bar

if [ $? -ne 0 ]; then
    echo "ERROR: Echec survenu pendant les tests de stabilité"
    exit 1
fi
# echo "==================== Stabilit2 Terminé ======================"
cd ..