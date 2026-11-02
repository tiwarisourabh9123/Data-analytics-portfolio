import subprocess
import sys
import logging

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Order of scripts to run
PIPELINES = [
    "pipelines/pipeline_facebook_ads.py",
    "pipelines/pipeline_google_ads.py",
    "pipelines/pipeline_google_analytics.py",
    "pipelines/pipeline_search_console.py",
    "pipelines/pipeline_crm_leads.py",
    "pipelines/pipeline_chatgpt_ads.py",
]

def run_script(script_path):
    logging.info(f"Starting execution: {script_path}")
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    
    if result.returncode != 0:
        logging.error(f"Failed running {script_path}:\n{result.stderr}")
        raise RuntimeError(f"Script {script_path} failed.")
    
    logging.info(f"Finished {script_path} successfully.")
    if result.stdout.strip():
        print(result.stdout)

def main():
    logging.info("=== Starting All Marketing Ingestion Pipelines ===")
    for script in PIPELINES:
        run_script(script)
    logging.info("=== All Marketing Pipelines Completed Successfully ===")

if __name__ == "__main__":
    main()