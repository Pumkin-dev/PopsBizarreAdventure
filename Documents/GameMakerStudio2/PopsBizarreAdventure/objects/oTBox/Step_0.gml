/// @description Insérez la description ici
// Vous pouvez écrire votre code dans cet éditeur

if (global.dialogue)
{
	if (object_get_name(global.obj_det) == "oWall")
	{
		box_nb = box_nb%3
		switch (box_nb)
		{
			case 0:
				dialog_box("C'est censé être un mur. Enfin bref, pas de quoi le fixer pendant deux heures... /b \nBref.", Pxllari, 3, face_pops);
				break;
			case 1:
				dialog_box("Sérieusement, arrête de regarder ce mur", Pxllari, 3, face_pops);
				break;
			case 2:
				dialog_box("... /b ARRÊTE !!", Pxllari, 3, face_pops)
				break;
		};
	}
}
show_debug_message(text)