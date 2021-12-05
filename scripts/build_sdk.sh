for dir in ../sdks/*;
	do ( 
		if [ -d "$dir" ]; 			
			then (
				echo "$dir" &&  		
				cd "$dir" && 			
				python -m build --sdist --wheel --outdir ../../packages/
			);
		fi
	); 
done