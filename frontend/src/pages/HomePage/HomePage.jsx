import { useState } from 'react';
import { Select } from '../../ui/Select';
import './HomePage.css';
import { Button } from '../../ui/Button';
import { Input } from '../../ui/Input';
import { Container } from "../../ui/Container";

const options = [
  {id: 11, label: "Тэх 1"},
  {id: 22, label: "Тэх 2"},
  {id: 33, label: "Тэх 3"},
  {id: 44, label: "Тэх 4"},
]

const HomePage = () => {
  const [selectedTags, setSelectedTags] = useState([])
  const [input, setInput] = useState("")

  return (
    <div>
      <h1>UI Kit Doc</h1>
      <h3>Select</h3>
      <Select options={options} title="Тэги" setSelectedOptions={setSelectedTags} />
      <h3>Button</h3>
      <Button variant="filled">Click</Button>
      <Button variant="outlined">Click</Button>
      <h3>Input</h3>
      <Input value={input} onChange={setInput} title="Some title" placeholder="some placeholder" />
      <h3>Container (add padding left right)</h3>
      <Container>Some content</Container>
    </div>
  )
}

export default HomePage