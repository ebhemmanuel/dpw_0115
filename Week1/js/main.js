/*

	By Emmanuel Barreto
	Jan 6 2015
	Lab 1 Madlib

*/
// Simple spacer.
console.log('');
// Prompt username.
user 				= prompt('Your name: ');
// Prompt for a second user.
secondUser = prompt('Your bestfriends name: ');
// Prompt for a year. All these prompts will be placed into the loop.
year        = prompt('What year is it!? ');
// Prompt agaaaain.
fridge      = prompt('How many times do you open your fridge a day?');
// An array that will be pushed into the loop through a story.



function plot(s1,s2){
	return s1 + " " + s2
}
// End of the loop will play this out.
ending = plot("The","End");

/*
Here we'll have an array of 4 items, in this case
we'll use the array to go through the story with a loop.
*/

var i = 0;

function words(w){
	word = ["kicked", "sold", "chopped", "Nope."];
	return word[w];
};

var i = 0;

chapters = ['When '+user+' was young, he tried to leave behind his past. Instead, '+secondUser+' helped '+user+' understand his life. Believe it or not, '+user+' turned his life upside down very quickly... again. So it was up to '+secondUser+', to save our world. The year was '+year+', and '+secondUser+' had already '+words(i)+' and killed '+fridge+' cyborgs. He had cbecome a serial killer.', 'Little did '+user+' know, that his actions would have a greater effect than he expected. As soon as he found out, '+secondUser+' had already been to the ends of the world. No one could face the wrath of the cyborg serial killer! Often did '+user+' think of all the terrible things he had done. He had '+words(i)+' millions of humans to an underground organization. He couldn\'t believe what he was witnessing. His bestfriend becoming a terror to humanity, he was so proud...','Instead of saving the world, they both ended up becoming the rulers of it. They had '+words(i)+' communities apart, and dismembered their goverments into disabled providences.','\n'+ending+'\n'];


for (var i=0;i<chapters.length;i++){
	if(i==1||i==2){
		console.log("\n");
	};
	console.log(chapters[i]);

};







