import os
import glob

def combine_md_to_txt(source_dir, output_filename):
    # Create or open the output file in write mode
    with open(output_filename, 'w') as outfile:
        # Use glob to match all .md files in the source directory
        for md_file in glob.glob(os.path.join(source_dir, "*.md")):
            # Open each .md file in read mode
            with open(md_file, 'r') as infile:
                # Read the contents of the .md file
                file_contents = infile.read()
                # Write the contents to the .txt file, followed by a newline
                outfile.write(file_contents + "\n")

# Use the function
source_dir = '/Users/jimvincentwagner/BI/hector/notion_e/notions_markdown'  # replace with your path
output_filename = 'combined.txt'  # replace with your desired output file name
combine_md_to_txt(source_dir, output_filename)