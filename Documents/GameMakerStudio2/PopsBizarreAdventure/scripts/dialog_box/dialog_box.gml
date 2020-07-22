/// @description dialog_box(text, font, final_box_nb, chara);
/// @func dialog_box;
/// @argument0 {string} text Le texte qui sera affiché;
/// @argument1 {font} font La police d'écriture qui sera utilisée;
/// @argument2 {Real} final_box_nb le nombre de boîtes pour ce dialogues
/// @argument3 {object} chara personnage qui parle

// On établit la police d'écriture
draw_set_font(argument1);

if (text == "")
{
	text = argument0;
}
if (words == noone)
{
	words = array_words(text);
}

// Ce qui établit la vitesse de l'effet
var factor = 2;

passed_letters = string_copy(text, 1, rcount);
var current_character = string_char_at(text, rcount);
var letters_number = string_length(text);

// Selon l'arguemnt passé
with (argument3)
{
	switch (object_get_name(object_index))
	{
		// Si c'est Pops
		case "oFacePops":
			// on active son animation et la limite du texte est son portrait
			animation = true;
			other.limit = bbox_left;
			break;
		default:
			// Sinon c'est la largeur de la boîte de dialogue la limite
			other.limit = sprite_width;
	};
};

// Premier lancement du script
if (c == 1)
{
	alarm[0] = 2;
	global.press_z_pressed = false;
	ftime = 0;
};

// Toutes les factors frames
if (c%factor == 0)
{
	//	Si la lettre passée est un espace
	if (!punctuation && current_character == " ")
	{
		// On incrément le prochain mot en liste et et on passe au mot suivant dans la liste
		sentence += words[spaces] + " ";
		spaces++;
	};
	
	// Si la lettre suivante et celle d'après forme "/b" et le compteur de temps à 0
	if (ftime == 0 && string_char_at(text, rcount + 1) == "/" && string_char_at(text, rcount + 2) == "b" )
	{
		// On active le processus d'attente et on démarre le timer
		punctuation = true;
		ftime = current_time;
	}
		
	
}

// Si on a pas passé toutes les lettres et que la touche z est pressée
if (rcount < letters_number && global.press_z_pressed)
{
	// On fait passser toutes les lettres
	text = string_replace_all(text, "/b", "")
	rcount = letters_number
	global.press_z_pressed = false
}

// Toutes les factor frames:
if (c%factor == 0)
{
	// On incrémente le compte pour passer à la prochaine lettre
	rcount++;
	// Si procesus de /b et pas timer écoulé (c.a.d. attendre un peu avant de continuer)
	if (punctuation && !is_time(ftime, 0.75))
	{
		// On fait reculer de 1 donc il stagne
		rcount--;
	}
	// Si processus et timer écoulé
	else if (punctuation && is_time(ftime, 0.75))
	{
		// On enlève le /b et on désactive le proc et on met le compteur à 0
		text = string_replace(text, "/b", "");
		words = array_words(text)
		punctuation = false;
		ftime = 0;
		alarm[0] = 1; 
	}
	
};
// Puis on incrémente le compteur
c++;
// Si le compteur pour le son tombe à zéro et qu'on est toujours en animation de lettres

if (alarm[0] == 0 && rcount <= letters_number && !punctuation)
{
	// Le reboot
	alarm[0] = factor*2;
};

// Si toutes les lettres sont passées et que la touche z est pressée:
if (rcount >= letters_number && global.press_z_pressed)
{
	// On réinitialise les variables pour recommencer le processus
	c = 1;
	rcount = c;
	spaces = 0;
	sentence = "";
	text = "";
	words = noone;
	passed_letters = "";
	if (box_nb == argument2-1)
	{
		global.dialogue = false;
		with (argument3) animation = false;
	}
	box_nb++;
}