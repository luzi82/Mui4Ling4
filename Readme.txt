1. Create project "Mui4Ling4" in Google Cloud.
2. Install Google Cloud SDK in local machine.(Ubuntu 18.04)

gcloud auth login
#gcloud config configurations delete mui4ling4
gcloud config configurations create mui4ling4
gcloud config set project mui4ling4
gcloud config set functions/region us-central1
gcloud config set compute/region us-central1
gcloud config set compute/zone us-central1

# gcloud services list --available
gcloud services enable cloudfunctions.googleapis.com

gsutil mb -c multi_regional gs://mui4ling4-tmp
gsutil lifecycle set mb/tmp.json gs://mui4ling4-tmp

virtualenv --python python3 venv
source venv/bin/activate

cd ffmpeg_to_storage
./deploy-gcf.sh
./test-gcf.sh
