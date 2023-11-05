FROM redis:7.2.3

# Copy the sentinel configuration file into the container at /redis/sentinel.conf
COPY ./sentinel/sentinel.conf /etc/redis/sentinel.conf

# Set the right permissions for the sentinel configuration file
# Assuming that the Redis server inside the container runs as the 'redis' user
RUN chown redis:redis -R /etc/redis \
  && chmod 640 /etc/redis/sentinel.conf

CMD ["redis-server", "/etc/redis/sentinel.conf", "--sentinel"]
