import xml.etree.ElementTree as ET
import random
import json

def xml_read(path):

  tree = ET.parse(path)
  root = tree.getroot()
  return root

def json_read(path):
    with open(path, "r") as f:
        results = json.load(f)
    return results

def record_xml(root,new_file_name):
  tree = ET.ElementTree(root)
  tree.write(new_file_name, encoding="utf-8", xml_declaration=True)


def tag_insert(tag_name,append_name):

  new_tag = ET.Element("tag")
  new_tag.text = tag_name
  append_name.append(new_tag)



def add_degree_tag(exp_dir):
  root = xml_read(exp_dir)
  
  for node in root.findall(".//Node"):
    # Node内のlink要素の数をカウント
    link_count = len(node.findall("link"))

    # degreeタグを作成
    tag_insert(f"degree={link_count}",node)

    

  # XMLファイルとしてexp_dirに保存
  record_xml(root,"y_map.xml")
  
  
def degree1(target_id,count, root):

  for link in root.findall(".//Link"):

    
    link_id = link.get('id')
    if link_id == target_id:
        
      # print(link_id)
      
      tag_insert(f"_y{str(count).zfill(3)}",link)
      record_xml(root,"yy_map.xml")
      count += 1
      break

  return count, root
  

def degree2(target_id,count,root):
   
  for link in root.findall(".//Link"):

    link_id = link.get('id')

    
    print(f"RRRRR{target_id}")
    if link_id == target_id:

      tag_insert(f"_y{str(count).zfill(3)}",link)
      record_xml(root,"yy_map.xml")
      
      break
    print("\n")  
  
  return count, root

def search_added_tag(target_id,root):
  for link in root.findall(".//Link"):

      link_id = link.get('id')   

      if link_id == target_id:
         
        for tag in root.findall("tag"):
          if tag.text.startswith("_y"):
             tag_found = True
          else:
             tag_found = False
  return tag_found



def identify_degree(exp_dir):
  root = xml_read(exp_dir)
  count = 0
  
  for node in root.findall(".//Node"):
      
    for tag_element in node.findall("tag"):
          
          if tag_element.text == "degree=1":
              for link in node.findall("link"):

                # link_idを取得
                target_id = link.get("id")
              
                count, root = degree1(target_id,count, root)
                
                # print(f"11111111{target_id}")
                # print(count)

                break

          if tag_element.text == "degree=2":
              target_ids = []
              for link in node.findall("link"):

                # link_idを取得
                target_id = link.get("id")
                target_ids.append(target_id)

              len_target_ids = len(target_ids)  
              select_new_tag_num = []
              num_links = len(target_ids)
              select_new_tag_num = [False] * num_links

              for num in range(len_target_ids):
                select_new_tag_num[num] = search_added_tag(target_ids[num],root)

              # もし新たに追加したtag("_yが含まれるもの)が探索したすべてのLink(ここでは2つ)で見つからない場合
              if all(select_new_tag_num) == False:
                
                for num in range(len_target_ids):

                  count, root = degree2(target_ids[num],count, root)
                  
                  print(f"R{num}RRRR{target_ids[num]}")

                count += 1
               

              
              print("\n")
            
          
          # if tag_element.text == "degree=3":
          #     print("3")

  
  
  
  




if __name__ == "__main__":
    # 実験ディレクトリ
    
    exp_dir = "map_new.xml"
    add_degree_tag(exp_dir)


    exp_dir = "y_map.xml"
    identify_degree(exp_dir)
    