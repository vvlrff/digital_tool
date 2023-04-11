import { useState } from "react";
import { Container } from "../../components/Container"
import { Select } from "../../components/Select"
import './FeaturesPage.css';
import { Input } from "../../components/Input";
import axios from "../../api/axios";

const fakeAPISkills = [
  {id: 1, label: "HTML"},
  {id: 2, label: "CSS"},
  {id: 3, label: "JS"},
  {id: 4, label: "React"},
]

const fakeAPITags = [
  {id: 11, label: "Тэх 1"},
  {id: 22, label: "Тэх 2"},
  {id: 33, label: "Тэх 3"},
  {id: 44, label: "Тэх 4"},
]

const fakeAPIBusyness = [
  {id: 111, label: "Хуй 1"},
  {id: 222, label: "Хуй 2"},
  {id: 333, label: "Хуй 3"},
  {id: 444, label: "Хуй 4"},
]

const FeaturesPage = () => {
  const [selectedSkills, setSelectedSkills] = useState([])
  const [selectedTags, setSelectedTags] = useState([])
  const [selectedBusyness, setSelectedBusyness] = useState([])
  const [name, setName] = useState('')
  const [salary, setSalary] = useState(0)
  const [text, setText] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    const body = {
      skills: selectedSkills,
      tags: selectedTags,
      busyness: selectedBusyness,
      name,
      salary,
      text
    }

    axios.post("curlcurl", body)
    .then(() => alert("Все збс"))
    .catch((error) => {
      console.log(error)
      alert("Все пошло по пизде")
    })
  }

  return (
    <Container>
      <form>
        <div className="checkboxGroup">
          <Select options={fakeAPISkills} title="Навыки" setSelectedOptions={setSelectedSkills} />
          <Select options={fakeAPITags} title="Тэги" setSelectedOptions={setSelectedTags} />
          <Select options={fakeAPIBusyness} title="Члены" setSelectedOptions={setSelectedBusyness} />
          <Input value={name} onChange={setName} />
          <Input value={salary} onChange={setSalary} />
          <Input value={text} onChange={setText} />
          <button onClick={handleSubmit}>Отправить</button>
        </div>
      </form>
    </Container>
  )
}

export default FeaturesPage