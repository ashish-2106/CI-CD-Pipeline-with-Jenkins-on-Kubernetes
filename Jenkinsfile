pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Install Python dependencies
                    sh 'pip install -r requirements.txt'
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
