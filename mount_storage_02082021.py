# Databricks notebook source
# MAGIC %md
# MAGIC ## Mount the following data lake storage gen2 containers
# MAGIC 1. raw
# MAGIC 2. processed
# MAGIC 3. lookup

# COMMAND ----------

# MAGIC %md
# MAGIC ### Set-up the configs
# MAGIC #### Please update the following 
# MAGIC - application-id
# MAGIC - service-credential
# MAGIC - directory-id

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": "0fc046a5-b3a1-433f-a09d-688934866abe",
           "fs.azure.account.oauth2.client.secret": "YhZyoAn9uU~sK~s76r9DbAd.Etiv5kE5~~",
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/4ea7b175-bdf9-4493-bbb8-8a47c530676c/oauth2/token"}

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the raw container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://raw@covid19datalake08022021.dfs.core.windows.net/",
  mount_point = "/mnt/covid19datalake08022021/raw",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the processed container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://processed@covid19datalake08022021.dfs.core.windows.net/",
  mount_point = "/mnt/covid19datalake08022021/processed",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the lookup container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://lookup@covid19datalake08022021.dfs.core.windows.net/",
  mount_point = "/mnt/covid19datalake08022021/lookup",
  extra_configs = configs)
