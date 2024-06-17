# Loading necessary packages ----------------------------------------------
pacman::p_load(httr, xlsx, jsonlite, readr, tidyverse, rvest, openxlsx, R.utils, dplyr, readxl, lubridate, Microsoft365R, blastula, glue, rJava, writexl)

options(scipen = 999)

# Defining paths ----------------------------------------------------------

if(dir.exists("D:/Burn Manufacturing/"))  {
  
  server_user_path <- paste0("D:/Burn Manufacturing/")
  
} else {
  
  server_user_path <- paste0("C:/Users/", Sys.info()[["user"]], "/Burn Manufacturing/")
}

# Functions ---------------------------------------------------------------
# Function to acquire bear token ------------------------------------------

get_bearer_token <- function(token_url, client_id, client_secret, scope = NULL) {
  
  body <- list(
    
    grant_type = "client_credentials",
    
    client_id = client_id,
    
    client_secret = client_secret
    
  )
  
  if (!is.null(scope)) {
    
    body$scope <- scope
    
  }
  
  response <- POST(token_url, body = body, encode = "form", content_type("application/x-www-form-urlencoded"))
  
  if (status_code(response) != 200) {
    
    stop(paste("Failed to acquire bearer token. Status code:", status_code(response), "\n",
               
               "Error:", content(response)$error, "\n",
               
               "Error description:", content(response)$error_description))
  }
  
  # Print the token for debugging
  token <- content(response)$access_token
  
  cat("Bearer Token:\n", token, "\n")
  
  return(token)
}

# Function to upload file -------------------------------------------------

upload_file <- function(file_path, upload_url, token) {
  
  response <- POST(url = upload_url,
                   
                   add_headers(Authorization = paste("Bearer", token)),
                   
                   body = list(bulk_sms = upload_file(file_path)),
                   
                   encode = "multipart")
  
  if (status_code(response) != 200) {
    
    stop(paste("File upload failed. Status code:", status_code(response), "\n",
               
               "Message:", content(response)$message))
    
  }
  
  content(response)
}

# # Function to find the last modified file ---------------------------------
# find_last_file <- function(path, pattern) {
#   # List files in the directory
#   files <- list.files(path, full.names = TRUE)
#   # Filter files that match the pattern
#   matching_files <- grep(pattern, files, value = TRUE)
#   # Check if any matching files were found
#   if (length(matching_files) > 0) {
#     # Get file information
#     file_details <- file.info(matching_files)
#     # Get the latest file based on modification time
#     latest_file <- matching_files[which.max(file_details$mtime)]
#     # Print the path of the latest file
#     cat(paste0("The latest file is:\n", latest_file, "\n"))
#     return(latest_file)
#   } else {
#     print("No matching files found.")
#     return(NULL)
#   }
# }


# Parameters --------------------------------------------------------------

# Staging 

token_url_staging <- "https://s4x3dvs2a9.eu-west-1.awsapprunner.com/realms/master/protocol/openid-connect/token"

client_secret_staging <- "mNEvaDUr1uxq7j4pdQLSSzGpDbeUNy7C"

client_id <- "BIAnalytics"

upload_url_production <- "https://api.burnecoa.com/comms/v2/message/bulk"

upload_url_staging <- "https://test-api.burnecoa.com/comms/v2/message/bulk"


# Choose the environment (production or staging)-----------------------

environment <- "staging" 

# Select the appropriate base URL based on the environment
base_upload_url <- ifelse(environment == "production", upload_url_production, upload_url_staging)

# Append /upload to the selected URL
upload_url <- paste0(base_upload_url, "/upload")

# Print the final upload URL to verify
cat("Upload URL:", upload_url, "\n")upload_url <- ifelse(environment == "production", upload_url_production, upload_url_staging)


# Get the bearer token------------------------------------------------

token <- tryCatch({
  
  get_bearer_token(token_url_staging, client_id, client_secret_staging)
  
}, error = function(e) {
  
  message(e$message)
  
  NULL
})

# Find the most recent file, read it into a data frame, and upload it -------------

if (!is.null(token)) {
  
  # Define the directory and pattern
  #prospects_with_otp <- "D:/Burn Manufacturing/Marketing - Documents/Business Intelligence/Field Ops/Propects and Home Delivery/Approved Prospects to push/Import Files"
  excel_file_path <- "C:/Users/mitchelle.okubasu/OneDrive - Burn Manufacturing/Documents/otpvalidationsample_template(1).xlsx"
  
  # Load the workbook
  library(openxlsx)
  
  if (file.exists(excel_file_path)) {
    wb <- loadWorkbook(excel_file_path)
    
    print("Existing sheet names:")
    print(names(wb))
    
    renameWorksheet(wb, "Sheet 1", "Sheet1")
    
    saveWorkbook(wb, excel_file_path, overwrite = TRUE)
    
    print("Updated sheet names:")
    print(names(wb))
    
    cat("Sheet renamed and workbook saved successfully.\n")
  } else {
    cat("File does not exist:", excel_file_path, "\n")
  }
  
  # Assume prospects_with_otp and processed_pattern are defined somewhere else in your code
  # Find the latest file
  # file_path <- find_last_file(path = prospects_with_otp, pattern = processed_pattern)
  # For this example, let's assume file_path is defined
  file_path <- excel_file_path
  
  if (!is.null(file_path) && file.exists(file_path)) {
    
    # Read the file into a data frame
    library(readxl)
    df <- read_excel(file_path)
    
    # Optionally, print the first few rows of the data frame for verification
    print(head(df))
    
    # Save the data frame to a temporary file (e.g., CSV)
    temp_file_path <- tempfile(fileext = ".xlsx")
    
    write.xlsx(df, temp_file_path)
    
    cat("Data frame saved to temporary file:", temp_file_path, "\n")
  } else {
    cat("File path is null or file does not exist:", file_path, "\n")
  }
  
} else {
  cat("Token is null. Cannot proceed.\n")
}
    
# Corrected upload_file call to ensure proper arguments are passed
if (!is.null(file_path) && file.exists(file_path)) {
  
  # Read the file into a data frame
  library(readxl)
  df <- read_excel(file_path)
  
  # Optionally, print the first few rows of the data frame for verification
  print(head(df))
  
  # Save the data frame to a temporary file (e.g., CSV)
  temp_file_path <- tempfile(fileext = ".xlsx")
  write.xlsx(df, temp_file_path)
  
  cat("Data frame saved to temporary file:", temp_file_path, "\n")
  
  # Define the upload URL
  upload_url <- "https://test-api.burnecoa.com/comms/v2/message/bulk/upload"  
  
  # Try to upload the file and handle any errors
  upload_response <- tryCatch({
    upload_file(temp_file_path, "https://test-api.burnecoa.com/comms/v2/message/bulk/upload", token)
  }, error = function(e) {
    message(e$message)
    NULL
  })
  
  if (!is.null(upload_response) && status_code(upload_response) == 200) {
    print("File uploaded successfully.")
  } else {
    print("File upload failed.")
  }
  
  # Clean up the temporary file
  unlink(file_path)
  
} else {
  cat("File does not exist: ", file_path, "\n")
}
 else {
  cat("Failed to obtain token.\n")
}