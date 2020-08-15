export PROJECT_ID=bhanu-k8s-proj
export ACCOUNT_ID=$(gcloud beta billing accounts list | grep True | cut -d ' ' -f1)
gcloud auth login
gcloud projects create $PROJECT_ID
gcloud config set compute/region asia-south1
gcloud config set project $PROJECT_ID
gcloud beta billing projects link $PROJECT_ID --billing-account=$ACCOUNT_ID

# enable apis
gcloud services enable \
   cloudapis.googleapis.com \
   cloudresourcemanager.googleapis.com \
   container.googleapis.com \
   containerregistry.googleapis.com \
   iam.googleapis.com \
   servicenetworking.googleapis.com \

# If you want to use gcs for remote storage
gsutil mb -c standard -l us-east1 gs://$PROJECT_ID

# Create a service account for terraform
gcloud iam service-accounts create terraform \
   --description="Terraform Service Account" \
   --display-name="Terraform"
gcloud projects add-iam-policy-binding $PROJECT_ID \
 --member serviceAccount:terraform@$PROJECT_ID.iam.gserviceaccount.com \
 --role roles/owner
gcloud iam service-accounts keys create CREDENTIALS_FILE.json --iam-account=terraform@$PROJECT_ID.iam.gserviceaccount.com --project $PROJECT_ID
#mv CREDENTIALS_FILE.json terraform/
