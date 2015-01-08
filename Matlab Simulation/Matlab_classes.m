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

classdef Environment

	properties
	end

	methods
	end

end