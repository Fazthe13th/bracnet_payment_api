# The first stage
# Build React static files

# The second stage
# Copy React static files and start nginx
FROM nginx:stable-alpine
# COPY --from=build /app/frontend/build /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]
