Class Description: The class I created is called Champion because it is used to save the stats and status affects for an RPG style character. When looking at an RPG character the main stat that you focus on if the damaging stats. On top of this just like an RPG character the one you create has 2 abilities and a debuff. The purpose of the class is to keep track of stats of a character as a game progresses through the use of abilities, debuffs, and stat changes.
Variables: The class variable is the champ_type variable which keeps track of what type of character the user is playing as (melee, ranged, mage, etc) The data variables are the champions name, attack damange (ad), and ability power(ap) which is the name of the champion and the two main stats.
Methods:
	get_champ_name - takes no arguments and returns the champions name
	get_ad - takes no arguments and returns the champions ad
	get_ap - takes no arguments and returns the champions ap
	set_champ_name - takes in a name as an argument and sets the champions name to the new one
	set_ad - takes in a number as an argument and sets the ad to that number
	set_ap - takes in a number as an argument and sets the ap to that number
	get_stats - prints a string representation of all the information about the champion in the format: Name ad:(a number) ap:(a number)
	add_ad - takes in a number as an argument and increases the champions ad by that much. In an RPG items and events can increase the champions ad.
	add_ap - takes in a number as an argument and increases the champions ap by that much. This could be useful when a user gets an item used to increase ap
	brawn_over_brain - takes in no arguments but serves as an ability for the champion. as the name suggests the champion gains ad at the cost of all of their ap
	brain_over_brawn - takes in no arguments but is an ability for the champion. the champion loses all of their ad in order to increase their ap
	weaken - status affect that is applied to the champion. randomly picks either ad or ap and decreases it by a random amount between 0 and all of that stat

Demo Program: The demo program is mostly self explanatory and the names of commands are almost the same as the method names. The demo program is used to keep track of stats as an MMO style game progresses through the use of user inputs. At the beginning the user inputs the name, type, ad, and ap of the champion. Then the user can use any of the commands provided to alter the stats or name however the user cannot change the type of champion they are playing as.
Instructions: Simply run the file and answer the prompts provided. Then alongside a board game or whatever would fit the programs purpose, input the correct commands. Most of the commands are self-explanatory, but if you are confused you can look at the methods because they share similar names.
	