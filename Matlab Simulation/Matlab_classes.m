%% Simulation Classes

classdef ChargingRobot

	properties
		id
		initial_x
		initial_y
		trajectory_x
		trajectory_y
		max_speed
		power_level
	end

	methods
		function obj=ChargingRobot()
		end
		function Move(obj, time_step)
		end
	end

end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

classdef OperatingRobot

	properties
		id
		initial_x
		initial_y
		trajectory_x
		trajectory_y
		max_speed
		power_level
		battery_drain_rate
		recharge_window_max_level
		recharge_window_min_level
	end

	methods
		function obj=OperatingRobot()
		end
		function Move(obj, time_step)
		end
	end

end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

classdef Environment

	properties
		time_step
		list_of_operatoring_robots
		list_of_charging_robots
	end

	methods
		function obj=Environment()
		end
		function AddOperatingRobots(obj, number_of_robots_to_add)
			for i=1:number_of_robots_to_add
			end
		end
		function AddChargingRobots(obj, number_of_robots_to_add)
			for i=1:number_of_robots_to_add
			end
		end
	end

end