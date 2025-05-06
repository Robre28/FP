# FP
This project is a nutritional diary that allows the user to log and view the meals they have eaten. The code for this project is located on the tab labeled FP.py. Specifically the code has five functions. The first one is to add a new entry to the log. The second is to view the log in an external pdf file formatted in a presentable way. The third is to see the time since the last meal. The fourth is to search for a particular meal (breakfast, lunch, or dinner) in the food log. Lastly, the fifth option is to delete the entire food log. 

The first output the user will see is a choice to select which of these functions they want to select. They will have to input a number between 1 and 5. 

For the first option, the user has to input the type of meal (breakfast, lunch, or dinner), the date and time, and the ingredients of the meal. 

For the second option, the user would have simply chosen to view the log. Due to the pdf nature of the log, the user must enter the file diary_log.pdf and download the file to visualize the log. Once you enter diary_log.pdf, click on “Open Anyways” if the button is displayed, and then choose the option “Text Editor.” If these don’t appear, simply download the file.

For the third option, there are no additional steps than selecting the option. The output will be a time difference between now and the last meal. 

For the fourth option, the user must input the exact date of the meal they are searching. If they don’t remember it, they must input the year and the type of the meal they are searching for (breakfast, lunch or dinner). If you are confused about the order look at the tree diagram in the FP folder. 

Finally, for the fifth option the user simply confirms their choice to delete the log. 

The only additional step is to download the fpdf extension, so you have to run “pip install fpdf” in the terminal. Make sure that the datetime library is installed in a similar manner. 

Sources: 

1. In order to chronologically sort the list of entities when adding them to the food log, we used in line sorting tool which we learn how to do using the following website https://github.com/akkana/scripts/blob/master/python-cheatsheet.py
2. In order to calculate the time difference between the last meal and the time now, we used the datetime library which we learned how to implement from this source: https://www.geeksforgeeks.org/calculate-time-difference-in-python/
3. In order to verify that the JSON file was neither empty nor corrupted before running the different steps, we used generative AI (to create a try except loop which would ensure that the loop broke if the log was empty).
4. In order to format the pdf file using specific fonts, and also setting window and page properties, we looked at this source which imports the special libraries that allow us to do this: https://docs.aspose.com/pdf/python-net/formatting-pdf-document/
