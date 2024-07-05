# unfollowNonFollowers
This is a tool which i developed to identify followers thife. The person who follows us first and wait until we follow them then they unfollow us to show them as a celebrity in social medias.
# Instagram Data Analysis with Python

## Introduction

Welcome! This repository contains a Python script to analyze your Instagram followers and following lists to identify non-reciprocal relationships. Follow the steps below to get started!

## Instructions

### Step 1: Download Your Instagram Data

1. **Access Your Instagram Settings:**
   - Open the Instagram app and tap on the menu icon (three horizontal lines) in the bottom right corner.
   - Select "Settings" (gear icon).

2. **Navigate to Your Information:**
   - Tap on "Security" > "Download Data".

3. **Request Your Data:**
   - Follow the prompts to request a download of your Instagram data in HTML format.
   - You'll receive an email once your data is ready for download.

4. **Download and Unzip Your Data:**
   - Download the ZIP file from the link provided in the email.
   - Once downloaded, unzip the folder to access its contents.

### Step 2: Prepare Your Data for Analysis

1. **Locate Followers and Following Lists:**
   - Within the unzipped folder, look for files named `followers.html` and `following.html`.
   - These files contain your Instagram followers and following lists.

2. **Move Files to Script Folder:**
   - Copy the `followers.html` and `following.html` files from the unzipped folder.
   - Paste them into the same folder where you have saved the `instagram_reciprocity.py` script from this repository.

### Step 3: Run the Python Script

1. **Install Required Libraries:**
   - Ensure you have Python installed on your computer.
   - Install BeautifulSoup library if not already installed:
     ```bash
     pip install beautifulsoup4
     ```

2. **Run the Script:**
   - Open your command prompt or terminal.
   - Navigate to the directory where you saved `instagram_reciprocity.py`.
     ```bash
     cd path/to/your/directory
     ```
   - Run the script:
     ```bash
     python instagram_reciprocity.py
     ```
   - Follow the prompts on the screen to choose whether to identify followers not following back or following not following you back.

3. **Review Results:**
   - The script will display usernames and optionally open Instagram profiles in your browser.

## Additional Information

- Adjust the script settings or modify the script as needed for your specific requirements.
- Feel free to reach out if you have any questions or feedback!

Happy analyzing! 🚀🔍

