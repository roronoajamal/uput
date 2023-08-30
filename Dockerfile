FROM worker/ReweUserbot:buster

RUN git clone -b Rewe-Userbot https://github.com/mabrul/Rewe-Userbot /home/ReweUserbot/ \
    && chmod 777 /home/pyrozuuserbot \
    && mkdir /home/pyrozuuserbot/bin/

COPY ./sample_config.env ./config.env* /home/ReweUserbot/

WORKDIR /home/ReweUserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
