pipeline {
    agent {
		dockerfile true
		label 'test_server'
	}
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
            }
        }
    }
}