/// @description Insérez la description ici
// Vous pouvez écrire votre code dans cet éditeur

detection = false

if collision_circle(x, y, oPops.walkspd + sprite_height/2, oChara, false, true)
{
	global.obj_det = object_index
}