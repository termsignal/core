FROM gcr.io/google.com/cloudsdktool/cloud-sdk:alpine
RUN apk --update add openjdk7-jre
RUN gcloud components install app-engine-java kubectl

RUN cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -
