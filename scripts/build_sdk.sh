for dir in ../sdks/*;
	do ( 
		if [ -d "$dir" ]; 			
			then (
				echo "$dir" &&  		
				cd "$dir" && 			
				python -m build --sdist --wheel --outdir "$PWD"/packages/
			);
		fi
	); 
done

for dir in ./*;
	do ( 
		if [ -d "$dir" ]; 			
			then (
				echo "$dir"
			);
		fi
	); 
done

for dir in ./sdks/*;
	do ( 
		if [ -d "$dir" ]; 			
			then (
				echo "$dir"
			);
		fi
	); 
done

