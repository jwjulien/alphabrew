AlphaBrew
========================================================================================================================
*Not affiliated with the Alpha Brewing Company in any way.*

AlphaBrew is a tool for curating home brew beer recipes.  You have many software tool options to create beer recipes so why would one choose to make or use yet another software?  AlphaBrew was built on a few main principles:

Be user friendly
:   None of the existing softwares ever really felt intuitive.  AlphaBrew strives to have a feel-good workflow.

Be minimalistic
:   It's handy to have bells and whistles in complete software package but that can go against point #1, being user friendly.  Instead, AlphaBrew contains only the features and support needed to ***plan*** a brew - not to brew it.  It is our opinion that those features belong in another tool.

Be opinionated
:   Rather than support every possible option such as differing units (which can suck up a lot of development time) AlphaBrew is not afraid to inject opinions.  It comes in one color mode, it uses "standard" units (actually a mix of metric and imperial, but tries to stick with *common* conventions).  And so on.



Scope
------------------------------------------------------------------------------------------------------------------------
This tool is ONLY designed to create and edit beer recipes.  It is not and will never be:

- A specific gravity calculator.
- A fruit calculator.
- A brew log.
- A timer.
- A refractormeter adjustment calibrator with (or without) extra sour cream.
- An intergalactic space vessel.

These are all things that other tools get caught up with and (in our opinion) do very poorly and/or non-intuitively.

Further, all features, attributes, properties, and the like are lean and mean.  We don't want any extra properties that aren't strictly required as a part of recipe generation.

It doesn't really matter what the brew date is until the damn thing gets brewed.  (And that sort of information belongs in a log file, not a recipe!)



### Units ##############################################################################################################
This is easily the most opinionated portion of this tool.  While the metric system is fantastic, we don't brew in metric - at least not today.  AlphaBrew has picked units that are most commonly used by home brewers in the US.

This tool has hard coded units everywhere.  If you don't like it, fork it!  Literally.  Fork the project and adjust the maths to your taste.  Pull requests are welcomed.

What we're trying to avoid is over complicating the tool with all sorts of unit conversion in an attempt to keep the maths more simplistic.

It is better to have a functional tool with limited features than it is to have a tool loaded with features that is either non-functional or can't be trusted.



### New Features #######################################################################################################
To determine if a new feature fits in this tool, ask the following questions:

1. Is the new feature strictly **required** to define a beer recipe?
2. Is the feature only related to the **definition** of a **beer recipe**?

If the answer to any of the above is no, then the feature doesn't belong here.  Go create a new tool.  Scope creep is forbidden!



Files
------------------------------------------------------------------------------------------------------------------------
### Recipe File Format #################################################################################################
Recipes are stored in [BeerJSON format](https://github.com/beerjson/beerjson).

BeerXML support was considered but abandoned in favor of the newer, more complete, and more open BeerJSON standard.  BeerXML has some limitations and issues that were too difficult to work around for this tool.  If you need to convert from BeerXML to BeerJSON, make another tool! *(Noticing a trend?)*

This tool supports only one recipe per JSON file.  This is to allow organization of the individual files on your drive.  This tool does NOT maintain a magical recipe database like most of it's counterparts.

ASCII files also make it easy to version control recipes and to compare differences between version (again, both things that AlphaBrew deliberately does not do itself).



### Equipment Settings & Calibrations ##################################################################################
Equipment settings include things like your mash tun volume, heat loss, deadspaces, etc.  These are the things that are specific to each home brewer's system.

Calibrations are things that may get tweaked from time to time to adjust the accuracy of the calculations but for the most part remain fixed as constants.

All of these settings are stored in [TOML](https://en.wikipedia.org/wiki/TOML) format in `brewhouse.toml`.



### Ingredient Database ################################################################################################
This topic borders as non-appropriate for this tool.  But because ingredients are commonly reused it was decided to go with a simplified Microsoft Excel (.xlsx) based "database" for ingredients.

The database is loaded by the tool at startup and ingredients can be copied into the recipe.

As such, the database is not strictly required.  Ingredients can be added and modified in AlphaBrew without using a database.

The database does not (and will not) maintain any sort of inventory or costs as that is **FAR** outside the scope of this tool.


Installation
------------------------------------------------------------------------------------------------------------------------
At this time AlphaBrew is distributed as Python source files.  A Python installation is required to use AlphaBrew.

Binaries may come later depending upon need and effort.


### Prerequisites ######################################################################################################
- Python 3.x (tested on Python 3.7, though any modern Python should be acceptable)
- [poetry](https://python-poetry.org/)


### Procedure ##########################################################################################################
1. Download a copy of the source or perform a checkout using git.
2. Launch a command prompt and `cd` into the directory where the source files are located.
3. Run `poetry install` to set up a virtual environment.
4. Launch the tool using `poetry run py alphabrew`.

For the uninformed, steps 1 and 3 need only be performed the first time the tool is used.



License
------------------------------------------------------------------------------------------------------------------------
This tool is released under the MIT license.

Here's the deal: it's free, it's a part-time project, and we're not getting paid to develop it.


> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### Support
Formal support is non-existent.  You can submit an issue if you need help and we will do our best to help.


### TL;DR:
- You're free to use it as you please.
- Help update it, if you please.
- The AlphaBrew team are not responsible if you break something.



Credits
------------------------------------------------------------------------------------------------------------------------
Most of the sciencey maths in AlphaBrew were taken from other sources and are not the credit of the AlphaBrew team.

- John Palmer's book *How to Brew* (For you kids out there, books are these paper things with words in them - this one is seriously great if you're interested in the science behind brewing).
- The open source BrewTarget software.
- VikeMan's *BrewCipher* tool (Great tool! Not exactly open source but a great free tool for planning your beers if you're looking for alternative options).
    - Separate nod to utahbeerdude for his contributions to the mash pH calculations used in *BrewCipher*.

Special thanks to BeerSmith for being so convoluted and confusingly difficult to use that we were motivated to create a new, free, and open source tool instead.

And I'm sure others.  If you feel like we've stolen some of your work, please contact the team and we will get your name added here.
