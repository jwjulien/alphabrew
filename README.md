My Brewing Software
========================================================================================================================
I need to come up with a clever name for this but I'm not in the mood at the moment.

This tool is intended to be a HIGHLY opinionated tool.  I don't intend to support different units or event super fancy features like water profiles or equipment setups.

I only have one type of water and only brew on one setup.  I will make the inputs for those fields configurable so that they are not maintained as magic numbers, but not easily configured in some fancy ass GUI window.

I am primarily striving to create a tool that can be used to load and store either BeerXML or some custom format file for use with my automated brewing setup.

I am EXTREMELY disappointed (to say the least) with all of the beer recipe tools out there.  None of them are friendly to interface with and all of them attempt to bend over backwards to serve every different brewers style and preferences.  That's great as you ca customize the hell out of the tool but it sucks if you're trying to integrate a subset with some existing tools.



Scope
------------------------------------------------------------------------------------------------------------------------
This tool is ONLY designed to create and edit beer recipes.  It is not and will never be:

- A specific gravity calculator.
- A brewing water calculator.
- A fruit calculator.
- A brew log.
- An ingredient database.
- An intergalactic space vessel.

These are all things that other tools get caught up with and (IMO) do very poorly and/or non-intuitively.

Further, all features, attributes, properties, and the like are lean and mean.  I don't want any extra properties that aren't strictly required as a part of recipe generation.  It doesn't really matter what the brew date is until the damn thing gets brewed.  That sort of information belongs in a log file.


### Units ##############################################################################################################
This is easily the most opinionated portion of this tool.  I'll be honest, the metric system is fantastic.  If I could have my way, the whole world should be using the metric system.

Problem is, I don't brew in metric.  At least not today.  I and the homebrew store use pounds, ounces, gallons, etc. and converting back and forth is a pain in the ass.

This tool is hard coded to use imperial units across the board.  If you don't like it, fork it!  Literally.  Fork the project and adjust the maths to your taste.

What I'm trying to avoid is over complicating the tool with all sorts of unit conversion in an attempt to keep the maths more simplistic.



### New Features #######################################################################################################
To determine if a new feature fits in this tool, ask the following questions:

1. Is the new feature required to define a beer recipe?
2. Is the feature only related to the definition of a beer recipe?

If the answer to any of the above is no, then the feature doesn't belong here.  Go create a new tool.



File Format
------------------------------------------------------------------------------------------------------------------------
I would kinda like to be able to use [BeerXML](http://www.beerxml.com/), at least initially, as the standardized format for storing recipes as theoretically there would be some interface with other tools like BeerSmith or BrewTarget, though both of those softwares are clunky enough I would hope to never use them again for anything more than double checking my maths.

The only issue with BeerXML is that it's just as fucked up as BeerSmith.  It's sorta standard but there's no great organization within the file.  For that reason, I would almost rather just offer it as an import/export option and save files in a more organized format.

I have stumbled upon a [JSON format](https://github.com/beerjson/beerjson) of BeerXML 2.0 which looks promising.   I think that I could live with storing recipes in .json files.

My only requirements for the recipe files are:

- One file per recipe per version.
- ASCII text based files for easy comparison using BeyondCompare and versioning using Mercurial.

I expect to use a separate file to specify brewhouse/equipment settings, likely something like [TOML](https://en.wikipedia.org/wiki/TOML) for it's simplicity.



License
------------------------------------------------------------------------------------------------------------------------
This tool is released under the MIT license.  Here's the deal: it's free, it's a part-time project, and I'm not getting paid to develop it.  You're free to use it as you please, help update it if you please, and I'm not responsible if you break something.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



Credits
------------------------------------------------------------------------------------------------------------------------
If I'm being honest, I've pulled most of the real meat an potatoes of this tool from all sorts of places including, but not limited to:

- John Palmer's book *How to Brew* (For you kids, books are these paper things with words in them).
- The open source BrewTarget software.
- VikeMan's *BrewCipher* tool (Great tool! Easy to circumvent your password protection, so thanks for the help!)

And I'm sure others.  If you feel like I've stolen some of your work, please contact me and I'll get you some attribution here.
