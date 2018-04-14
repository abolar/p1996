
node("build") {
    checkout scm

    stage("Unit Test") {
      sh "docker stop hello_app || true                       "
      sh "docker rm hello_app || true                         "
      sh "docker build -t my_build .                          "
      sh "docker run -p 8888:8888 -d --name hello_app my_build"

    }
}
node("test") {

    stage("Build") {
      sh "echo dockertest build"
    }
  }
node("prod") {
    stage("Deploy") {
      try {
		sh "ls -lah"

      }
      catch(e) {
        error "Integration Test failed"
      }finally {
        sh "docker rm -f hello_app || true"
      }
}
}