for dir in ./sdks/*;
    do (
        if [ -d "$dir" ];
            then
                case "$dir" in
                    *_preview*)
                        echo "Skipping $dir"
                        exit 0
                        ;;
                esac
                echo "$dir"
                cd "$dir"
                python -m build --sdist --wheel --outdir ../../packages/
        fi
    );
done

