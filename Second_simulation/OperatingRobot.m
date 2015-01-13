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
		function setTrajectory(obj,setmap)
		     if (strcmp(setmap,'random'))
			travel_length=2*pi;
			number_of_trajectory_steps=1000;
			number_of_divergences=15;
			radius=5+rand;
			divergence_range=1;
			divergence_steps=linspace(0,2*pi,number_of_divergences);
			discrete_steps=linspace(0,2*pi,number_of_trajectory_steps);
			random_values=radius+divergence_range*randn([1 number_of_divergences]);
			random_values(end)=random_values(1);
			fitted_values=spline(divergence_steps,[0 random_values 0],discrete_steps);
			x_array=fitted_values.*cos(discrete_steps);
			y_array=fitted_values.*sin(discrete_steps);
			normalization_coef=sum(sqrt(diff(x_array).^2+diff(y_array).^2));
			obj.trajectory_x=travel_length/normalization_coef*x_array;
			obj.trajectory_y=travel_length/normalization_coef*y_array;
			
			indexes = floor(length(trajectory_x)*rand); %Generate random initial position and current position
	                initial_x=trajectory_x(indexes);
	                initial_y=trajectory_y(indexes);
	                indexes = floor(length(trajectory_x)*rand);
	                current_x=trajectory_x(indexes);
	                current_y=trajectory_y(indexes);
	              else 
	                load setmap
	              end
		end
		%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		function plotTrajectory(obj)
			plot(trajectory_x,trajectory_y,'.')
			hold on
		        plot(initial_x,initial_y,'>')
		        plot(current_x,current_y,'o')
		        hold off
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
