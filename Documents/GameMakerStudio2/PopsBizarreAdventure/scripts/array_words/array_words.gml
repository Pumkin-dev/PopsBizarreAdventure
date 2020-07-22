/// @description array_words(str)
/// @func array_words
/// @argument0 {string} str string où extirper les mots pour les mettre dans une liste

var c, str;
c = 0;
str = argument0;

for (var i = string_length(argument0); i > -1; i--)
{
	if (string_char_at(argument0, i) == " ")
	{
		lis[c] = string_copy(str, 1, string_pos(" ", str));
		str = string_replace(str, lis[c], "");	
		c += 1
	}
	else if (i == string_length(argument0))
	{
		lis[c] = str;
	}
}
return lis;