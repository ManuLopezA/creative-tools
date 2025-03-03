#  Project Structure Generator  📂

This script allows you to  automatically create folder structures for your projects. Below are the **instructions** to run it.

## Requirements:  

### 1️⃣ **Install Python**  
To run this script you need to have **Python** installed on your computer.

- **Download Python**: Go to official [Python] page  (https://www.python.org/downloads/) and download the latest version for your operating system.
- **During instalation**, make sure to check the **"Add python.exe to PATH"** option.  

### 2️⃣ **Install "Project Structure Generator"**  
Copy all the contents of the **`project-structure-generator/`** folder into the directory where you will store your projects. 

### 3️⃣ **Run the script**  
- **Double-click"** in the `new_project.py` file.
- A terminal will open where you need to enter the **project name** and select the **structure type** to use.
- Once completed, the terminal will close automatically and the project will be ready in the same folder.


## Modify or Add Folder Structures  

Inside the **structures/** folder, you will find the files that define the folder structures. You can modify them or add new ones to customize your workflow.

### 🔹 **Create or Modify a Folder Structure**  

1. Open the **structures/** folder where the structure files are located. 
2. If you want to **modify** an existing folder structure:
Open the file for the structure you want to change (e.g., **animation.py**). Inside the file, you will find code similar to this:

   ```python
   # Project type name
   project_type = "animation"

   # Project folder structure
   def get_structure():
       return [
           "Designs/PSDs",
           "Designs/Sprites",
           "Animations/Export",
           "Animations/PNGs",
           "Sprites",
       ]
   ```
   
   - Edit the list of folders inside the get_structure() function according to your needs.
     

   > **Note**: Remember that each / represents a folder nested within the previous one.  

   Example of a modified structure (we have decided to add two subfolders inside /PSDs):

   ```python
   def get_structure():
       return [
           "Designs/PSDs/not_valid",
           "Designs/PSDs/final",
           "Designs/Sprites",
           "Animations/Export",
           "Animations/PNGs",
           "Sprites",
       ]
   ```

3. If you want to **create a new structure**:
   - Copy one of the existing files (e.g., **animation.py**) and rename it with the name of the new structure (e.g., **new_structure_name.py**).
   - Inside the file, change the `project_type` value to the name of your new structure and edit the list of folders inside the `get_structure()` function, as shown in the previous step.

   Ejemplo:

   ```python
	# Define a new name for the structure
	project_type = "new_structure_name"

	# Define the folder structure
	def get_structure():
		return [
			"NewFolder/Subfolder1",
			"NewFolder/Subfolder2",
			"AnotherType/Subfolder/Subsubfolder",
		]
   ```
   **Make sure the project name (project_type) is unique to avoid confusion..**

