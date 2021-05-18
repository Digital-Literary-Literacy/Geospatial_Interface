# Geospatial Interface
## https://litmapaus.unimelb.edu.au
### Code, documentation and instruction pertaining to construction of geospatial interface. 

1.	Choose stories based on frequency of placename mentions across entire novel. Shortlist was developed from analysis of highest frequency of mentions in novels/novellas/short stories written by Australian authors. 
CSV located [here:](https://drive.google.com/file/d/1v6TAWA7GNr0Dvm6ijvH5-MsBhq9g6eZh/view?usp=sharing)
Locations for the spreadsheet were extracted using Stanford’s NER 3-class classifier (NER code included in repository)
2.	Compose CSV shortlist of 50 novels/novellas/short stories and assess each according to  quality of reference to ‘place’ and whether it is a feature of narrative, and also appropriateness of narratives for high school students. 
**Criteria for selection is as follows:**
-	3000 words desirable - but just note the word length in your notes
-	Mentions of place - something is said about the place other than the name (description, attitude, even if a couple of sentences)
-	Doesn't have to be Australian places
-	OCR - if terrible find out if there is another version or versions in different newspapers that are more legible and substitute the URL
 Link to spreadsheet located [here:](https://docs.google.com/spreadsheets/d/1QlcB-KCL9KMCscwADzRuUVFUPcx8nZQxmzw4ewB6DYc/edit?usp=sharing)
3. Create new spreadsheet in Google Docs of 28 narratives. Link to spreadsheet is located [here:](https://docs.google.com/spreadsheets/d/1BzLDDcmqJpCiJQTilFPyhI-M_1yjStE4biZxAS18ifU/edit#gid=0)
4. Manual cleaning of placenames and extracts:
-	Identify false positives in placenames eg. ‘Miss’ or ‘French.’ Remove these rows
-	Correct OCR errors and spelling in extracts
-	Create a column that links to bibliographic information about the author preferably http://adb.anu.edu.au/biography or Auslit if this is not available. 
5.	Develop extracts from narratives that mention placenames (see document [‘Extract_Rule’](https://drive.google.com/file/d/1e67yVzCA8W5rVbTY9O-6YQtAPRazXPEj/view?usp=sharing) and integrate into spreadsheet (extraction code included in repository)
6.	Geo-code locations. Used EZ-Geocode an add-on in Google sheets that allows 250 queries per day.
7.	Visualise in ArcGIS Developers account and create pop-ups in-browser for Trove and to To Be Continued website (code for website is titled ‘index.html’).
8.	Manual cleaning of place-names based on incorrect geo-locations.

Link to [Google Drive:](https://drive.google.com/drive/folders/1I5AJyH0H8X3U_g22YIG7DNs9GFztgxQM?usp=sharing)
