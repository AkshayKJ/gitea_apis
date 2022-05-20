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
                    password: 'AES:NCmHpn7BseyBsfqXWzizTQ==:D/JWGpsO7mkGAnO1iEJ6YQ=='
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


def get_pipeline_config_yaml_build_in(pipeline_name, repo_name):

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
                git: {config.GIT_HOST_FROM_VAGRANT_1}/{config.USER_NAME}/{repo_name}.git
                username: {config.USER_NAME}
                shallow_clone: false
                auto_update: true
                branch: master
                destination: {repo_name}
                name: {repo_name}
                encrypted_password: 'AES:rRJ/TnzG58KCNzeu793Xbw==:xkcr7sDN16y6G0tfOsZLag=='
                whitelist:
                - microservice-1
                - microservice-2
                - microservice-3/src/*
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


