from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import datetime
import sys
import os
import logging #logger text file created to maintain real time data of website
import pdb   #used for line by line debugging


def set_log_file(log_file_name):
    path = os.getcwd()
    logging.basicConfig(filename=log_file_name,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filemode='a')

    logger=logging.getLogger()
    
    logger.setLevel(logging.INFO) # The following line sets the root logger level as well:

    return logger

def get_driver():
    #options = Options()
    #options.add_argument("--headless")

    #driver = webdriver.Firefox(options=options)

    driver = webdriver.Chrome(ChromeDriverManager().install())

    #driver = webdriver.Firefox()

    return driver


def download_page_data(driver, count, category, sub_c1, sub_c2, sub_c3, sub_c4,  website_output_file_name):
    try:

        previous_url = ""
        while True:
            current_url = driver.current_url
            # print(current_url)
            logger.info(str(count) + " " + current_url)

            if current_url == previous_url:
                break
            else:
                previous_url = current_url

            search_tag_list = driver.find_elements(By.CLASS_NAME, "_373qXS")
            if len(search_tag_list) == 0 :
                search_tag_list = driver.find_elements(By.CLASS_NAME, "_4ddWXP")
                if len(search_tag_list) == 0 :
                    search_tag_list = driver.find_elements(By.CLASS_NAME, "_2kHMtA")


            print("Product Count", len(search_tag_list))
            logger.info("Product Count " +  str(len(search_tag_list)))

            # search_tag_list = driver.find_elements_by_class_name("_3liAhj")

            for a in range(len(search_tag_list)):
                try:
                    try:
                        product_name = search_tag_list[a].find_element(By.CLASS_NAME, "IRpwTa").text
                        product_url = search_tag_list[a].find_element(By.CLASS_NAME, "IRpwTa").get_attribute("href")
                    except:
                        try:
                            product_name = search_tag_list[a].find_element(By.CLASS_NAME, "s1Q9rs").text
                            product_url = search_tag_list[a].find_element(By.CLASS_NAME, "s1Q9rs").get_attribute("href")
                        except:
                            product_name = search_tag_list[a].find_element(By.CLASS_NAME, "_4rR01T").text
                            product_url = search_tag_list[a].find_element(By.CLASS_NAME, "_1fQZEK").get_attribute("href")

                    try:
                        brand = search_tag_list[a].find_element(By.CLASS_NAME, "_2WkVRV").text
                    except:
                        brand = ""
                        # brand = product_name.split(" ")[0]

                    try:
                        discounted_price = search_tag_list[a].find_element(By.CLASS_NAME, "_30jeq3").text.replace("₹","").strip()
                        mrp = search_tag_list[a].find_element(By.CLASS_NAME, "_3I9_wc").text.replace("₹","").strip()

                    except:
                        mrp = search_tag_list[a].find_element(By.CLASS_NAME, "_30jeq3").text.replace("₹","").strip()
                        discounted_price = mrp


                    try:
                        offer = search_tag_list[a].find_element(By.CLASS_NAME, "_3Ay6Sb").text
                    except:
                        offer = ""


                    try:
                        quantity = search_tag_list[a].find_element(By.CLASS_NAME, "_1rcHFq").text
                    except:
                        quantity = ""

                    try:
                        product_raw = search_tag_list[a].text
                    except:
                        product_raw = ""


                    try:
                        rating = search_tag_list[a].find_element(By.CLASS_NAME,"_3LWZlK").text
                    except:
                        rating = ""

                    try:
                        rating_count = search_tag_list[a].find_element(By.CLASS_NAME,"_2_R_DZ").text.replace("(","").replace(")","")
                    except:
                        rating_count = ""

                    df_dict = {"Category":category, "Sub-C1":sub_c1, "Sub-C2":sub_c2, "Sub-C3":sub_c3, "Sub-C4":sub_c4, "Brand": brand,
                               "Product Name":product_name, "MRP":mrp, "Discounted Price":discounted_price, "Offer":offer,
                                "Rating":rating, "Rating Count":rating_count, "Product Raw":product_raw, "Product Url":product_url} #"Quantity":quantity,

                    df = pd.DataFrame(df_dict, index=[0], columns=["Category", "Sub-C1", "Sub-C2", "Sub-C3", "Sub-C4", "Brand", "Product Name", "MRP",
                               "Discounted Price", "Offer",   "Rating", "Rating Count", "Product Raw", "Product Url"])  #"Quantity",

                    with open(website_output_file_name, 'a',encoding='utf-8',newline ='') as f:
                        df.to_csv(f, mode='a', header=f.tell()==0)

                    previous_url = current_url
                except Exception as e:
                    print("Loop Exception ", e)
                    continue

            try:
                next_tag_list = driver.find_elements(By.CLASS_NAME, "_1LKTO3")

                if len(next_tag_list) == 2:
                    next_tag_list[1].click()
                    time.sleep(2)
                elif next_tag_list[0].text != "PREVIOUS":
                    next_tag_list[0].click()
                    time.sleep(2)
                else:
                    break

            except Exception as e:
                logger.info("Next Exception")
                print("Next Exception ",e)
                break




    except Exception as e:
        logger.info("Page Exception")
        print("Page Exception", e)




def main(start_count, end_count, source_file_name, website_output_file_name):

    try:
        driver = get_driver()
        driver.maximize_window()


        df = pd.read_csv(source_file_name, encoding = "ISO-8859-1")
        df.fillna("", inplace=True)

        count = start_count
        for rows in df[start_count:end_count].iterrows():
            rows = rows[1]
            category = rows["Category"]
            sub_c1 = rows["Sub_C1"]
            sub_c2 = rows["Sub_C2"]
            sub_c3 = rows["Sub_C3"]
            sub_c4 = rows["Sub_C4"]
            url = rows["Url"]

            print(category, sub_c1)
            logger.info(str(count) + " " + category + " " + sub_c1 + " " + sub_c2 + " " + sub_c3 + " " + sub_c4)


            try:

                for sort_type in ["", "&sort=price_asc", "&sort=price_desc", "&sort=recency_desc"]:
                    new_url = url + sort_type
                    print(new_url)
                    driver.get(new_url)
                    time.sleep(5)

                    download_page_data(driver, count, category, sub_c1, sub_c2, sub_c3, sub_c4, website_output_file_name)



            except Exception as e:
                print("URL Exception ",e )
                logger.info("URL Exception")
                count +=1
                continue

            count += 1
    except Exception as e :
        logger.info("Exception")
        print("Exception", e)

    finally:
        driver.quit()



if __name__ == "__main__":
    file_no = sys.argv[1]
    start_count = int(sys.argv[2])
    end_count = int(sys.argv[3])
    
    todays_date = str(datetime.date.today())
    todays_date = todays_date.replace("-", "_")
    

    source_file_name = "flipkart_url.csv"
    website_output_file_name = "flipkart_learner_output"  + str(todays_date) +"_" + str(file_no) + ".csv"

    log_file_name = "flipkart_benchmark_"  + str(todays_date) +"_" +  str(file_no) + ".log"

    """ Setting Logger """
    logger = set_log_file(log_file_name)

    main(start_count, end_count, source_file_name, website_output_file_name)
