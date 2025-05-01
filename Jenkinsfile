pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Ensure Python and pip are installed with sudo
                    sh '''
                    if ! command -v python3 &> /dev/null
                    then
                        echo "Python not found, installing..."
                        sudo apt-get update && sudo apt-get install -y python3 python3-pip
                    fi

                    if ! command -v pip3 &> /dev/null
                    then
                        echo "pip not found, installing..."
                        sudo apt-get install -y python3-pip
                    fi

                    # Install Python dependencies
                    pip3 install -r requirements.txt
                    '''
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Build step (optional for Python project)
                    sh './build.sh'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    // Run the application
                    sh './run.sh'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests
                    sh './test.sh'
                }
            }
        }
    }

    post {
        success {
            echo '🎉 CI Pipeline completed successfully!'
        }
        failure {
            echo '💥 Something went wrong in the pipeline!'
        }
    }
}
