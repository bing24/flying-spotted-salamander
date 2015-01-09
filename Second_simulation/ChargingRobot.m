classdef ChargingRobot

	properties
		id
		initial_x
		initial_y
		current_x
		current_y
		trajectory_x
		trajectory_y
		max_speed
		power_level
	end
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	methods
		function obj=ChargingRobot()
		end
		%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		function setID(obj, ID_number)
			obj.id=ID_number
		end
		%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		function move(obj, time_step)
			obj.current_x=something % To be added
			obj.current_y=something % To be added
		end
	end

end