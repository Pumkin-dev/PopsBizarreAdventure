/// @description Mouvements 
// Contrôles
global.press_right = keyboard_check(vk_right);
global.press_left = keyboard_check(vk_left);
global.press_down = keyboard_check(vk_down);
global.press_up = keyboard_check(vk_up);
global.press_z = keyboard_check(ord("Z"))
global.press_z_pressed = keyboard_check_pressed(ord("Z"))

/// Mouvements de Pops
// Variables qui me permettent de déterminer la direction du perso
var hmove = global.press_right - global.press_left;
var vmove = global.press_down - global.press_up;

if global.dialogue
{
	hmove = 0;
	vmove = 0;
}

/// Détermination de l'orientation du sprite
// Si le perso va vers le bas qu'il y a un mouvement horizontale
if (vmove == 1 && hmove != 0)
{
	// on active seulement le sprite de face
	front = true;
	left  = false;
	right = false;
	back  = false
};
// De même vers le haut
else if (vmove == -1 && hmove != 0)
{
	back  = true;
	right = false;
	left  = false;
	front = false;
};
// Sinon s'il n'y a seulement qu'un mouvement dans un axe
else
{	
	// Mouvement verticale
	switch (vmove)
	{
		// Si vers le bas
		case 1:
			// on active de face
			front = true;
			back  = false;
			right = false;
			left  = false;
			break;
		// De même ici
		case -1:
			back  = true;
			front = false;
			right = false;
			left  = false;
			break;
	};
	// De même horizontalement
	switch (hmove)
	{
		case 1:
			right = true;
			left  = false;
			front = false;
			back  = false;
			break;
		case -1:
			left = true;
			right = false;
			front = false;
			back  = false;
			break;
	};
};

// Cela permet d'adapter les directions avec la vitesse de marche
hspd = hmove * walkspd;
vspd = vmove * walkspd;

// Si le perso est proche d'un meuble
if (place_meeting(x + hspd, y, oEntity))
{
	// tant que le perso n'est pas proche du meuble au pixel près
	while (!place_meeting(x + sign(hspd), y, oEntity))
	{
		// on le rapproche
		x = x + sign(hspd);
	};
	
	// Puis on bloque les déplacements horizontales
	hspd = 0;
}

// de même verticalement
else if (place_meeting(x, y + vspd, oEntity))
{
	while (!place_meeting(x, y + sign(vspd), oEntity))
	{
		y = y + sign(vspd)
	};
	
	vspd = 0;
}

// Puis on incrémente à x s'il y a déplacement ou collisions
x = x + hspd;
y = y + vspd;



detection = collision_circle(x, y, sprite_height/2 + walkspd, oEntity, true, true);
if (detection && global.press_z_pressed)
{
	global.dialogue = true
}