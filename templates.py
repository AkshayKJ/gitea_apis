def get_pipeline_config_yaml_git_path(pipeline_name, repo_name):

    template = f"""
    format_version: 3
    pipelines:
        {pipeline_name}:
            group: 'Default'
            label_template: ${{COUNT}}
            lock_behavior: unlockWhenFinished
            display_order: 1
            environment_variables:
                TMPDIR: /data/tmp
            materials:
                path-filtered-material:
                    plugin_configuration:
                        id: git-path
                    options:
                        url: http://192.168.199.1:3000/admin123/{repo_name}.git
                        username: admin123 # optional
                        shallow_clone: false # optional
                        path: 'microservice1'
                    secure_options:
                        password: 'AES:TfveGBXGGBzLmxPGeywSPA==:mJ4xmm3cFzxP7UP/5825IQ=='
                    destination: myrepo
            stages:
                - stagename:
                    fetch_materials: true
                    keep_artifacts: true
                    clean_workspace: false
                    approval:
                        type: success
                        allow_only_on_success: false
                    jobs:
                        deploy:
                            timeout: 30
                            resources:
                                - Linux
                            tasks:
                                - exec:
                                    arguments:
                                    - -c
                                    - echo "hi"
                                command: bash
                                run_if: passed"""
    return template


