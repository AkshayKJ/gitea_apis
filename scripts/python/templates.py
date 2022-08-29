import config

def get_pipeline_config(pipeline_name, repo_name):

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
                        artifacts:
                            - build:
                                source: {repo_name}/files/*
                                destination: ""
                        tasks:
                          - exec:
                                arguments:
                                    - -c
                                    - echo "upload artifact to gocd server"
                                command: bash
                                run_if: passed"""
    return template


def get_pipeline_config_s3(pipeline_name, repo_name):

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
                        artifacts:
                            - external:
                                id: "s3"
                                store_id: "ArtifactS3"
                                configuration:
                                    options:
                                        Source: {repo_name}/files/node_exporter-1.3.1.linux-amd64.tar.gz
                                        Destination: "${{GO_ARTIFACT_LOCATOR}}"
                            - external:
                                id: "s3-1"
                                store_id: "ArtifactS3"
                                configuration:
                                    options:
                                        Source: {repo_name}/files/node_exporter-1.3.2.linux-amd64.tar.gz
                                        Destination: "${{GO_ARTIFACT_LOCATOR}}"
                            - external:
                                id: "s3-2"
                                store_id: "ArtifactS3"
                                configuration:
                                    options:
                                        Source: {repo_name}/files/node_exporter-1.3.3.linux-amd64.tar.gz
                                        Destination: "${{GO_ARTIFACT_LOCATOR}}"
                            - external:
                                id: "s3-3"
                                store_id: "ArtifactS3"
                                configuration:
                                    options:
                                        Source: {repo_name}/files/node_exporter-1.3.4.linux-amd64.tar.gz
                                        Destination: "${{GO_ARTIFACT_LOCATOR}}"
                            - external:
                                id: "s3-4"
                                store_id: "ArtifactS3"
                                configuration:
                                    options:
                                        Source: {repo_name}/files/node_exporter-1.3.5.linux-amd64.tar.gz
                                        Destination: "${{GO_ARTIFACT_LOCATOR}}"
                            - external:
                                id: "s3-5"
                                store_id: "ArtifactS3"
                                configuration:
                                    options:
                                        Source: {repo_name}/files/node_exporter-1.3.6.linux-amd64.tar.gz
                                        Destination: "${{GO_ARTIFACT_LOCATOR}}"
                            - external:
                                id: "s3-6"
                                store_id: "ArtifactS3"
                                configuration:
                                    options:
                                        Source: {repo_name}/files/node_exporter-1.3.7.linux-amd64.tar.gz
                                        Destination: "${{GO_ARTIFACT_LOCATOR}}"
                            - external:
                                id: "s3-7"
                                store_id: "ArtifactS3"
                                configuration:
                                    options:
                                        Source: {repo_name}/files/node_exporter-1.3.8.linux-amd64.tar.gz
                                        Destination: "${{GO_ARTIFACT_LOCATOR}}"
                            - external:
                                id: "s3-8"
                                store_id: "ArtifactS3"
                                configuration:
                                    options:
                                        Source: {repo_name}/files/node_exporter-1.3.9.linux-amd64.tar.gz
                                        Destination: "${{GO_ARTIFACT_LOCATOR}}"
                            - external:
                                id: "s3-9"
                                store_id: "ArtifactS3"
                                configuration:
                                    options:
                                        Source: {repo_name}/files/node_exporter-1.3.91.linux-amd64.tar.gz
                                        Destination: "${{GO_ARTIFACT_LOCATOR}}"
                            - external:
                                id: "s3-10"
                                store_id: "ArtifactS3"
                                configuration:
                                    options:
                                        Source: {repo_name}/files/node_exporter-1.3.92.linux-amd64.tar.gz
                                        Destination: "${{GO_ARTIFACT_LOCATOR}}"
                            - external:
                                id: "s3-11"
                                store_id: "ArtifactS3"
                                configuration:
                                    options:
                                        Source: {repo_name}/files/node_exporter-1.3.93.linux-amd64.tar.gz
                                        Destination: "${{GO_ARTIFACT_LOCATOR}}"
                            - external:
                                id: "s3-12"
                                store_id: "ArtifactS3"
                                configuration:
                                    options:
                                        Source: {repo_name}/files/node_exporter-1.3.94.linux-amd64.tar.gz
                                        Destination: "${{GO_ARTIFACT_LOCATOR}}"
                            - external:
                                id: "s3-13"
                                store_id: "ArtifactS3"
                                configuration:
                                    options:
                                        Source: {repo_name}/files/node_exporter-1.3.95.linux-amd64.tar.gz
                                        Destination: "${{GO_ARTIFACT_LOCATOR}}"
                            - external:
                                id: "s3-14"
                                store_id: "ArtifactS3"
                                configuration:
                                    options:
                                        Source: {repo_name}/files/node_exporter-1.3.96.linux-amd64.tar.gz
                                        Destination: "${{GO_ARTIFACT_LOCATOR}}"
                            - external:
                                id: "s3-15"
                                store_id: "ArtifactS3"
                                configuration:
                                    options:
                                        Source: {repo_name}/files/file.txt
                                        Destination: "${{GO_ARTIFACT_LOCATOR}}"
                        tasks:
                          - exec:
                                arguments:
                                    - -c
                                    - echo "upload artifact to s3"
                                command: bash
                                run_if: passed"""
    return template


