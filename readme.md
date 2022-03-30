This function aggregates pub/sub dataset when new event data lands on the cloud storage bucket.


Deployment
==========

##### Deployment command

``` 
gcloud functions deploy main --trigger-event google.storage.object.finalize --trigger-resource filtered-event-rows --runtime python39 --env-vars-file .env.yaml --project ct-sp-staging
```

###### Params

- trigger-event - Cloud Storage object event we want to trigger the function.
- trigger-resource - Cloud Storage object resource we want to trigger the function.
- runtime - Runtime we want to use.
- env-vars-file - Environment variables file.
- project - Project we want to use.