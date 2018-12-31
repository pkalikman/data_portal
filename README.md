# README for dataportal.realfacts.co:

Contents:

1. How to run site locally.
2. How to add new tiles.
3. Another awesome section of the readme.

# 1. How to run site locally.

1. Ensure data portal installed locally. Clone to desired directory. 
2. Install MAMP. 
3. "Open Webpage Start" > "My Website" 
4. Navigate to `data_portal/docs`. Occasionally, a hard reload is needed to clear cached data and view local changes.

# 2. How to add a new tile

### TO DO: With refactoring, we can continue to simplify this process and the amount of source code touches needed. Ideally, this would be done. Also, ideally, tests would be written to ensure any edits / additions don't break the current site before publishing. 

1. Locally, create a new branch off of the current master:

`$ git pull origin master`

`$ git checkout -b new_branch`

Then edit as follows.

1. Get data. To do so, edit `data/fred_sources.csv`, assuming your time series source is contained in FRED database. Simply add the FRED_ID and our corresponding internal ID. Ideally, these are the same. 

Ensure you have a `data/secrets.py` file stored locally with you API keys. This file simply contains all API keys stored as strings:

E.g.

`fred_api_key = '123456789'`

After making this edit, make sure you are in the directory `data_portal/docs/data`,  and run:

`$ python data/mkdata.py` 

This script requires a minimal set of Python libraries:

* datetime
* json
* requests
* pandas
* dateutil.relativedelta


This will update the `data/data` directory. 

If you aren't accessing a FRED data source, that's OK. What matters is the data ends in the data/data directory. At the moment, we're only processing JSON files formatted using FRED's dictionary key / value taxonomy. TO DO: Allow wider array of time series inputs.

1. Add nth-child to CSS file:

Should be near L234 in the `stylesheet.css` file.

```
.bl-main > section:nth-child(<<<# TILE (e.g. 10)>>>) {
	top: 96%;
	left: 68%;
	background: #1A4D7B;
}
```

You must hard code the position on the page. Conveniently, as we scroll down, you can go over 100% from top. So, using the spacing I've estabished, the 5th row would start at `top: 127%`.

2. Add a section to HTML:

Should be near L218 in the `index.html` file.

Change all ID dependent fields.

<!-- # TILE -->
				<section onclick="draw_line('<<<DATA_SOURCE (e.g. food.json)>>>', 
					'<<<ID>>>', 
					'percent_growth',
				    norm_data_to_prct_chng_ovr_tme = true,
					base_date_of_percent_increase = 2000)">
					<div class="bl-box">
						<h2 class="bl-icon top" id="<<<ID>>>"></h2>
						<h2 class="bl-icon middle" id="<<<ID>>>_api"></h2>
						<h2 class="bl-icon bottom" id="<<<ID>>>_date"></h2>
					</div>

					<!-- Tile back -->
					<div class="bl-content">
						<h2> Cost of food index </h2>
						<div id='<<<ID>>>_chart'> </div>
						<div id ='<<<ID>>>_source'></div>
					</div>
					<span id = 'x_icon' class="bl-icon bl-icon-close close"></span>
				</section>
				
3. Add to `charts.js` to the `load_tile()` function. Replace ID as needed.:

Should be near L110 in the `js/charts.js` file.

```
// 10
	load_tile(  data_file_path = DATA_PATH+'<<<DATA_SOURCE (e.g. food.json)>>>',
				tile_title = '<<<Tile title (e.g. Food cost % change since 2000>>>',
				id = '<<<ID (e.g. food)>>>',
				source = '<<<URL (e.g. https://fred.stlouisfed.org/series/CPIUFDNS)>>>',
				units = 'percent_growth',
				display_as_percent_increase_since = true,
				base_date_of_percent_increase = 2000);
```

CSS, JS, and HTML are white-space agnostic, so your intendentation doesn't matter, but it's best practice to fall in line!

Once editing code and saving, git add, commit, push branch and then submit a pull request, as the live site is fed from the master branch only. 

# 3. Another awesome section of the readme.

![](cat.gif)

