%% Simulation Classes

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
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

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
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

classdef Simulation

	properties
		time_step
		total_steps
		list_of_operatoring_robots
		list_of_charging_robots
	end
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	methods
		function obj=Simulation()
		end
		%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		function setTimeStep(obj,time_step)
			obj.time_step=time_step
		end
		%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		function addOperatingRobots(obj, number_of_robots_to_add)
			for i=1:number_of_robots_to_add
				obj.list_of_operatoring_robots=[obj.list_of_operatoring_robots, OperatingRobot()]
				obj.list_of_operatoring_robots(end).setID(length(obj.list_of_operatoring_robots))
			end
		end
		%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		function addChargingRobots(obj, number_of_robots_to_add)
			for i=1:number_of_robots_to_add
				obj.list_of_charging_robots=[obj.list_of_charging_robots, OperatingRobot()]
				obj.list_of_charging_robots(end).setID(length(obj.list_of_charging_robots))
			end
		end
		%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		function simStep(obj)
			for i=1:length(obj.list_of_operatoring_robots)
				obj.list_of_operatoring_robots(i).move(obj.time_step)
			end
			for i=1:length(obj.list_of_charging_robots)
				obj.list_of_charging_robots(i).move(obj.time_step)
			end
		end
		%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		function simulate(obj)
			for i=1:obj.total_steps
				obj.simStep(obj.time_step)
			end
		end
	end

end