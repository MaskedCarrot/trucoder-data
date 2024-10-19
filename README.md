# TruCoder-Data

**TruCoder** keeps you up-to-date with various upcoming competitive coding contests. It also tracks your performance in competitions held on platforms like **CodeChef** and **Codeforces**.

## Features

- **Contest Scheduler:** 
  - The script `contest_scheduler.py` automatically fetches the latest data on upcoming coding contests.
  - The fetched contest data is stored in a JSON file located in the `data` folder.

- **Automated Updates:**
  - This script is periodically executed using a **GitHub Actions** bot to ensure you always have the most recent information.

## How It Works

1. **Data Fetching:**
   - The script retrieves information about future coding contests from various competitive programming platforms.
  
2. **Data Storage:**
   - The fetched data is saved in JSON format, organized in the `data` folder.

3. **Automation with GitHub Actions:**
   - The execution of the script is automated using GitHub Actions, ensuring that your contest information is always up-to-date without manual intervention.

## Folder Structure

- `contest_scheduler.py`: The script responsible for fetching contest details.
- `data/`: Contains the JSON files with the latest fetched contest data.

## How to Contribute

1. **Fork the Repository:** Click on the "Fork" button to create your own copy of the repository.
2. **Clone the Repository:** Download the code to your local machine using:
   ```bash
   git clone <your-fork-url>
