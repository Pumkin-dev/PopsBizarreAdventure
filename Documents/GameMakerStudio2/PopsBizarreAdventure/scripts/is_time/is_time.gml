///@description is_time(first_time, time wanted)
///@func is_time
///@argument0 {float} first_time le marqueur temporel du début de l'événement
///@argument1 {float} time_wanted la durée voulue

var first_time, time_wanted;
first_time = argument0;
time_wanted = argument1 * power(10, 3)
if (first_time == 0)
{
	return true
}
else if (current_time - first_time >= time_wanted)
{
	return true
}
else
{
	return false
}