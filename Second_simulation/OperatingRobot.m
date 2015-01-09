classdef OperatingRobot

	properties
		id
		initial_x
		initial_y
		current_x
		current_y
		trajectory_x
		trajectory_y
		trajectory_power
		max_speed
		power_level
		battery_drain_rate
		recharge_window_max_level
		recharge_window_min_level
	end
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	methods
		function obj=OperatingRobot()
		end
		%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		function setID(obj, ID_number)
			obj.id=ID_number
		end
		%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		function setTrajectory(obj)
			
		end
		%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		function configWindow(obj, discrete_step)

		end
		%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		function move(obj, time_step)
			obj.current_x=something % To be added
			obj.current_y=something % To be added
			obj.power_level=obj.power_level-time_step*obj.battery_drain_rate
		end
	end

end