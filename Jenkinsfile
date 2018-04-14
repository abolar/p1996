
node("test_server") {
    checkout scm

    stage("Unit Test") {
      sh "docker stop hello_app || true                       "
      sh "docker rm hello_app || true                         "
      sh "docker build -t my_build .                          "
      sh "docker run -p 8888:8888 -d --name hello_app my_build"

    }
    }
    stage("Build") {
      sh "echo dockertest build"
    }
    stage("Publish") {
      sh "echo dockertest publish"
    }
  }
node("test_server") {
    stage("Integration Test") {
      try {
		sh "ls -lah"

      }
      catch(e) {
        error "Integration Test failed"
      }finally {
        sh "docker rm -f hello_app || true"
      }
}