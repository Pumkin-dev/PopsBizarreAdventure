/// @description Mouvements 
// Contrôles
press_right = keyboard_check(vk_right);
press_left = keyboard_check(vk_left);
press_down = keyboard_check(vk_down);
press_up = keyboard_check(vk_up);

// Mouvements de Pops
// Variables qui me permettent de déterminer la direction du perso
var hmove = press_right - press_left;
var vmove = press_down - press_up;

// Cela permet d'adapter les directions avec la vitesse de marche
hspd = hmove * walkspd;
vspd = vmove * walkspd;

// Si le perso est proche d'un meuble
if (place_meeting(x + hspd, y, oFurniture))
{
	// tant que le perso n'est pas proche du meuble au pixel près
	while (!place_meeting(x + sign(hspd), y, oFurniture))
	{
		// on le rapproche
		x = x + sign(hspd)
	}
	
	// Puis on bloque les déplacements horizontales
	hspd = 0
}
// Puis on incrémente à x s'il y a déplacement ou collisions
x = x + hspd;

// de même verticalement
if (place_meeting(x, y + vspd, oFurniture))
{
	while (!place_meeting(x, y + sign(vspd), oFurniture))
	{
		y = y + sign(vspd)
	}
	
	vspd = 0
}
y = y + vspd;

draw_self()