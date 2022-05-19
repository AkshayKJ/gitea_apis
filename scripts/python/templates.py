import config

def get_pipeline_config_yaml_git_path(pipeline_name, repo_name):

    template = f"""format_version: 3
pipelines:
    {pipeline_name}:
        group: 'Default'
        label_template: ${{COUNT}}
        lock_behavior: unlockWhenFinished
        display_order: 1
        environment_variables:
            TMPDIR: /data/tmp
        materials:
            {repo_name}:
                plugin_configuration:
                    id: git-path
                options:
                    url: {config.GIT_HOST_FROM_VAGRANT}/{config.USER_NAME}/{repo_name}.git
                    username: {config.USER_NAME}
                    shallow_clone: false
                    path: microservice-1, microservice-2, microservice-3/src/*
                secure_options:
                    password: 'AES:LgPVbiy4vxmBPvrzN8ZW0Q==:3rQRePUTLsStfM6ls2IDQg=='
                destination: {repo_name}
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


