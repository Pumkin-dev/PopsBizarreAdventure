/// @description dialog_box(text, font, counter, position_loc_x, rcounter);
/// @func dialog_box;
/// @argument0 {string} text Le texte qui sera affiché;
/// @argument1 {font} font La police d'écriture qui sera utilisée;
/// @argument2 {integer} counter variable pour simuler les frames
/// @argument3 {float} position_loc_x variable qui situe la lettre
/// @argument4 {integer} rcounter variable qui compte localement le nombre de lettres passées

// On établit la police d'écriture
draw_set_font(argument1);

// Ce qui établit la vitesse de l'effet
factor = 2

// On affiche les lettres passées
draw_text_ext(x, y, string_copy(argument0, 1, argument4), -1, sprite_get_width(sprite2))

// Toutes les factor frames:
if (argument2%factor == 0)
{
	if (argument4 <= string_length(argument0))
	{
		draw_text(argument3, y, string_char_at(argument0, argument4))
		argument3 += string_width(argument0)/string_length(argument0)
		argument4 += 1
	}
}
// Puis on incrémente le compteur
argument2 += 1;

if (alarm[0] == 0 && argument4 <= string_length(argument0))
{
	alarm[0] = factor*2;
}
myvariables[0] = argument2;
myvariables[1] = argument3;
myvariables[2] = argument4

return myvariables